import { Readable } from 'stream'
import { finished } from 'stream/promises'
import fs from 'fs';

async function downloadFiles(fileList = []){

    for (let index = 0; index < fileList.length; index++) {
        console.log(`Downloading ${index+1}/${fileList.length}:`, fileList[index])
        try {
            const fileUrlSplit = fileList[index].split('/');
            const fn = fileUrlSplit[fileUrlSplit.length-1];
    
            const stream = fs.createWriteStream(`./census_data_new/${fn}`);
            const { body } = await fetch(fileList[index]);
            await finished(Readable.fromWeb(body).pipe(stream));
            
        } catch (error) {
            continue;
        }
        
    }   
}

async function getData(){
    let data = await fetch('https://censusindia.gov.in/nada/index.php/api/tables/data/global/census_tables/1500/0/?ft_query=');
    let resp = await data.json();
    return resp;
}

async function run(){;
    let page = await getData();
    let fileList = [];

    for (let index = 0; index < page?.data.length; index++) {
        const ele = page.data[index];
        let data = {
            id: ele.table_id,
            t: ele.title,
            l: []
        }

        if (Object.keys(ele).includes('links')){
            data['l'] = data['l'].concat(ele.links[0].link)
        }
        if (Object.keys(ele).includes('items')){
            data['l'] = data['l'].concat(ele.items.map(e=>e.links[0].link).flat())
        }
        fileList.push(data);
    }

    // let stringified = JSON.stringify(fileList)
    // await writeFile('./census_filelist.json',stringified);
    // stringified = ''; // release memory.

    await downloadFiles(fileList.map(e=>e.l).flat());

}


run();