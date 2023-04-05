import {writeFileSync} from "fs";
import bfj from "bfj";
let LIMIT = 100;
let db = [];

async function saveText(text){
    writeFileSync('./out.json', text);
}

async function bfjStringify(data){
    console.log('stringifying')
    let promise = new Promise((res, rej) => {

        bfj.stringify(data)
            .then(jsonString => {
                res(jsonString)
            })
            .catch(error => {
                console.error('bfjStringify.error', error);
                rej(error)
            });

    });
    let result = await promise;
    return result;
}
async function bfjParse(path){
    let promise = new Promise((res, rej) => {
        let readStream = fs.createReadStream(path);
        bfj.parse(readStream)
            .then(jsonString => {
                res(jsonString)
            })
            .catch(error => {
                console.error('bfjParse.error', error);
                rej(error)
            });

    });
    let result = await promise;
    return result;
}

async function getPage(page = 0){
    console.log('getting page', page)
    let data =  await fetch(`https://data.gov.in/backend/dmspublic/v1/resources?format=json&limit=${LIMIT}&offset=${page*LIMIT}&sort[published_date]=desc`, {
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-GB,en;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "sec-ch-ua": "\"Brave\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "sec-gpc": "1"
        },
        "referrer": "https://data.gov.in/resources",
        "referrerPolicy": "same-origin",
        "body": null,
        "method": "GET",
        "mode": "cors",
        "credentials": "include"
      });
      let resp  = await data.json();
      return resp;
}   
async function run(){

    let pageCnt = 21;
    let page = await getPage(pageCnt);
    while (page?.data?.rows?.length > 0) {
        db = db.concat(page?.data?.rows)
        pageCnt+=1;
        page = await getPage(pageCnt);
    }
    console.log(page);
    bfjStringify(db).then(saveText)
}
run()


//  CSV

let LIMIT = 1000;
let csv = ``;

async function saveText(text){
    const blob = new Blob([text], {type: 'csv'});
    const fileUrl = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.download = 'name.csv';
    link.href = fileUrl;
    link.click();
}

async function getPage(page = 0){
    console.log('getting page', page)
    let data =  await fetch(`https://data.gov.in/backend/dmspublic/v1/resources?format=json&limit=${LIMIT}&offset=${page*LIMIT}&sort[published_date]=desc`, {
        "headers": {
          "accept": "application/json, text/plain, */*",
          "accept-language": "en-GB,en;q=0.9",
          "sec-ch-ua": "\"Brave\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"",
          "sec-ch-ua-mobile": "?0",
          "sec-ch-ua-platform": "\"macOS\"",
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "sec-gpc": "1"
        },
        "referrer": "https://data.gov.in/resources",
        "referrerPolicy": "same-origin",
        "body": null,
        "method": "GET",
        "mode": "cors",
        "credentials": "include"
      });
      let resp  = await data.json();
      return resp;
}   
async function run(){

    let pageCnt = 0;
    let page = await getPage(pageCnt);
    let header = Object.keys(page?.data?.rows[0]).toString();
    csv = header;

    while (page?.data?.rows?.length > 0) {
        for (let index = 0; index < page?.data?.rows?.length; index++) {
            const row = page?.data?.rows[index];
            const newRow =   {
                "_language": row?._language?.toString()?.replaceAll(',', '||') || false,
                "cdos_state_ministry": row?.cdos_state_ministry?.toString()?.replaceAll(',', '||') || false,
                "is_high_value_dataset": row?.is_high_value_dataset?.toString()?.replaceAll(',', '||') || false,
                "is_priced": row?.is_priced?.toString()?.replaceAll(',', '||') || false,
                "is_rated": row?.is_rated?.toString()?.replaceAll(',', '||') || false,
                "is_webservice": row?.is_webservice?.toString()?.replaceAll(',', '||') || false,
                "node_alias": row?.node_alias?.toString()?.replaceAll(',', '||') || false,
                "node_cdo_email": row?.node_cdo_email?.toString()?.replaceAll(',', '||') || false,
                "ogdp_download_count": row?.ogdp_download_count?.toString()?.replaceAll(',', '||') || false,
                "ogdp_view_count": row?.ogdp_view_count?.toString()?.replaceAll(',', '||') || false,
                "published_date": row?.published_date?.toString()?.replaceAll(',', '||') || false,
                "catalog_reference": row?.catalog_reference?.toString()?.replaceAll(',', '||') || false,
                "catalog_title": row?.catalog_title?.toString()?.replaceAll(',', '||') || false,
                "catalog_uuid": row?.catalog_uuid?.toString()?.replaceAll(',', '||') || false,
                "changed": row?.changed?.toString()?.replaceAll(',', '||') || false,
                "created": row?.created?.toString()?.replaceAll(',', '||') || false,
                "datafile": row?.datafile?.toString()?.replaceAll(',', '||') || false,
                "domain": row?.domain?.toString()?.replaceAll(',', '||') || false,
                "domain_visibility": row?.domain_visibility?.toString()?.replaceAll(',', '||') || false,
                "external_api_reference": row?.external_api_reference?.toString()?.replaceAll(',', '||') || false,
                "field_from_api": row?.field_from_api?.toString()?.replaceAll(',', '||') || false,
                "field_high_value_dataset": row?.field_high_value_dataset?.toString()?.replaceAll(',', '||') || false,
                "field_public": row?.field_public?.toString()?.replaceAll(',', '||') || false,
                "field_resource_type": row?.field_resource_type?.toString()?.replaceAll(',', '||') || false,
                "field_show_export": row?.field_show_export?.toString()?.replaceAll(',', '||') || false,
                "file_format": row?.file_format?.toString()?.replaceAll(',', '||') || false,
                "file_size": row?.file_size?.toString()?.replaceAll(',', '||') || false,
                "frequency": row?.frequency?.toString()?.replaceAll(',', '||') || false,
                "govt_type": row?.govt_type?.toString()?.replaceAll(',', '||') || false,
                "granularity": row?.granularity?.toString()?.replaceAll(',', '||') || false,
                "is_api_available": row?.is_api_available?.toString()?.replaceAll(',', '||') || false,
                "ministry_department": row?.ministry_department?.toString()?.replaceAll(',', '||') || false,
                "nid": row?.nid?.toString()?.replaceAll(',', '||') || false,
                "note": row?.note?.toString()?.replaceAll(',', '||') || false,
                "reference_url": row?.reference_url?.toString()?.replaceAll(',', '||') || false,
                "resource_category": row?.resource_category?.toString()?.replaceAll(',', '||') || false,
                "sector": row?.sector?.toString()?.replaceAll(',', '||') || false,
                "sector_resource": row?.sector_resource?.toString()?.replaceAll(',', '||') || false,
                "title": row?.title?.toString()?.replaceAll(',', '||') || false,
                "uuid": row?.uuid?.toString()?.replaceAll(',', '||') || false,
                "vid": row?.vid?.toString()?.replaceAll(',', '||') || false,
            }
            try {
                csv+= '\n' + Object.values(newRow).join(',')
                
            } catch (error) {
                console.error('skipping', error, pageCnt, index, newRow, page?.data?.rows[index])
            }
        }
        pageCnt++;
        page = await getPage(pageCnt);

    }
    saveText(csv);
}
run()


// 0-76
// 511-X