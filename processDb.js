import { open, writeFile } from 'fs/promises';

function sum(ar) {
    var sum = 0;
    for (var i = 0; i < ar.length; i++) {
      if(typeof ar[i] == `number`) sum += ar[i];
    }
    return sum;
  }
 
async function read() {
    const file = await open('/Users/anudit/Downloads/datagovcomplete.csv');
    let datafiles = [];
    let totalRows = 0;

    let header = false;
    for await (const line of file.readLines()) {
        totalRows++;
        if (header === false) header = true
        else {
            const sp = line.split(',');
            datafiles.push({
                fs: sp[26], //file_size
                t: sp[38], // title
                df: sp[16] // data_file
            })
        }
    }

    datafiles = datafiles.filter(e=>e.df!="false").filter(e=>Boolean(e.df));

    let fsSum = sum(datafiles.map(e=>parseInt(e.fs)).filter(Boolean));

    const stats = {}
    for (let index = 0; index < datafiles.length; index++) {
        const filename = datafiles[index]['df'].split('.');
        if (filename){
            const extension = filename[filename.length-1].toLowerCase()
            if (Object.keys(stats).includes(extension)) stats[extension]+=1
            else stats[extension]=1
        }
    }
    console.log({...stats, totalRows, valid: datafiles.length, fsSum: parseInt(fsSum/(1000*1000*1000)) + ' GB'});

    let stringified = JSON.stringify(datafiles)
    await writeFile('./datafile.json',stringified);

}
 

read()

// {
//     csv: 402254,
//     xls: 2012,
//     xml: 3285,
//     apk: 3,
//     'csv?versionid=105166540146881': 1,
//     'csv?versionid=105166540103233': 1,
//     'csv?versionid=105166540048065': 1,
//     'csv?versionid=105166539831361': 1,
//     'csv?versionid=105166540080769': 1,
//     'csv?versionid=105166540026497': 1,
//     'csv?versionid=105166540288001': 1,
//     'csv?versionid=105166540188033': 1,
//     'csv?versionid=105166540166337': 1,
//     'csv?versionid=105166540228161': 1,
//     'csv?versionid=105166540007745': 1,
//     'csv?versionid=105166540263169': 1,
//     'csv?versionid=105166540209217': 1,
//     'csv?versionid=105166539429953': 1,
//     'csv?versionid=105166539986689': 1,
//     'csv?versionid=105166539452993': 1,
//     'csv?versionid=105166539316801': 1,
//     'csv?versionid=105166539913729': 1,
//     'csv?versionid=105166540126977': 1,
//     'csv?versionid=105166539943937': 1,
//     'csv?versionid=105166539883137': 1,
//     'csv?versionid=105166539392577': 1,
//     'csv?versionid=105166539964801': 1,
//     'csv?versionid=105166539235009': 1,
//     'csv?versionid=105166539337857': 1,
//     'csv?versionid=105166539531009': 1,
//     'csv?versionid=105166539863233': 1,
//     'csv?versionid=105166539662209': 1,
//     'csv?versionid=105166539497665': 1,
//     'csv?versionid=105166539610561': 1,
//     'csv?versionid=105166539477313': 1,
//     'csv?versionid=105166539740481': 1,
//     'csv?versionid=105166539809921': 1,
//     'csv?versionid=105166539711233': 1,
//     'csv?versionid=105166539551169': 1,
//     'csv?versionid=105166539186497': 1,
//     'csv?versionid=105166539786689': 1,
//     'csv?versionid=105166539636289': 1,
//     'csv?versionid=105166539580033': 1,
//     'csv?versionid=105166539412033': 1,
//     'csv?versionid=105166539761857': 1,
//     'csv?versionid=105166539364481': 1,
//     'csv?versionid=105166539279105': 1,
//     'csv?versionid=105166539121025': 1,
//     'csv?versionid=105166539297409': 1,
//     'csv?versionid=105166538901697': 1,
//     'csv?versionid=105166539143297': 1,
//     'csv?versionid=105166538945857': 1,
//     'csv?versionid=105166539683585': 1,
//     'csv?versionid=105166539163969': 1,
//     'csv?versionid=105166538881601': 1,
//     'csv?versionid=105166539099329': 1,
//     'csv?versionid=105166539032449': 1,
//     'csv?versionid=105166538922561': 1,
//     'csv?versionid=105166539213825': 1,
//     'csv?versionid=105166538679041': 1,
//     'csv?versionid=105166538831233': 1,
//     'csv?versionid=105166539256065': 1,
//     'csv?versionid=105166539080513': 1,
//     'csv?versionid=105166538701249': 1,
//     'csv?versionid=105166538753601': 1,
//     'csv?versionid=105166538967681': 1,
//     'csv?versionid=105166538990145': 1,
//     'csv?versionid=105166538788993': 1,
//     'csv?versionid=105166538617537': 1,
//     'csv?versionid=105166538637377': 1,
//     'csv?versionid=105166538657473': 1,
//     'csv?versionid=105166539059329': 1,
//     'csv?versionid=105166538771777': 1,
//     'csv?versionid=105166538853249': 1,
//     'csv?versionid=105166538812289': 1,
//     'csv?versionid=105166539011009': 1,
//     'csv?versionid=105166538736129': 1,
//     'csv?versionid=105166538495873': 1,
//     'csv?versionid=105166536856193': 1,
//     'csv?versionid=105166538597057': 1,
//     'csv?versionid=105166538568577': 1,
//     'csv?versionid=105166538541889': 1,
//     'csv?versionid=105166538518849': 1,
//     'csv?versionid=105166538473985': 1,
//     'csv?versionid=105166538424513': 1,
//     'csv?versionid=105166538042177': 1,
//     'csv?versionid=105166538402945': 1,
//     'csv?versionid=105166538449857': 1,
//     'csv?versionid=105166538123201': 1,
//     'csv?versionid=105166538195009': 1,
//     'csv?versionid=105166538351425': 1,
//     'csv?versionid=105166538066945': 1,
//     'csv?versionid=105166538380929': 1,
//     'csv?versionid=105166538302593': 1,
//     'csv?versionid=105166537996417': 1,
//     'csv?versionid=105166537954753': 1,
//     'csv?versionid=105166537914305': 1,
//     'csv?versionid=105166537672769': 1,
//     'csv?versionid=105166538222145': 1,
//     'csv?versionid=105166538283521': 1,
//     'csv?versionid=105166538258817': 1,
//     'csv?versionid=105166538170945': 1,
//     'csv?versionid=105166538021121': 1,
//     'csv?versionid=105166538326081': 1,
//     'csv?versionid=105166537866241': 1,
//     'csv?versionid=105166537885569': 1,
//     'csv?versionid=105166537815937': 1,
//     'csv?versionid=105166537787329': 1,
//     'csv?versionid=105166537973953': 1,
//     'csv?versionid=105166537840385': 1,
//     'csv?versionid=105166537739969': 1,
//     'csv?versionid=105166537585601': 1,
//     'csv?versionid=105166538092673': 1,
//     'csv?versionid=105166538150785': 1,
//     'csv?versionid=105166537306689': 1,
//     'csv?versionid=105166537443393': 1,
//     'csv?versionid=105166537559873': 1,
//     'csv?versionid=105166537934401': 1,
//     'csv?versionid=105166537530625': 1,
//     'csv?versionid=105166537618817': 1,
//     'csv?versionid=105166537192897': 1,
//     'csv?versionid=105166537501185': 1,
//     'csv?versionid=105166537353665': 1,
//     'csv?versionid=105166537761665': 1,
//     'csv?versionid=105166537404673': 1,
//     'csv?versionid=105166537334337': 1,
//     'csv?versionid=105166537041217': 1,
//     'csv?versionid=105166537289601': 1,
//     'csv?versionid=105166537374977': 1,
//     'csv?versionid=105166536997889': 1,
//     'csv?versionid=105166537476481': 1,
//     'csv?versionid=105166537709313': 1,
//     'csv?versionid=105166537168961': 1,
//     'csv?versionid=105166537134017': 1,
//     'csv?versionid=105166536911169': 1,
//     'csv?versionid=105166536172929': 1,
//     'csv?versionid=105166536819777': 1,
//     'csv?versionid=105166537151361': 1,
//     'csv?versionid=105166537267073': 1,
//     'csv?versionid=105166537058945': 1,
//     'csv?versionid=105166536782273': 1,
//     'csv?versionid=105166536892865': 1,
//     'csv?versionid=105166537424449': 1,
//     'csv?versionid=105166536124481': 1,
//     'csv?versionid=105166536158657': 1,
//     'csv?versionid=105172445945729': 1,
//     'csv?versionid=105166536933889': 1,
//     'csv?versionid=105172445745665': 1,
//     'csv?versionid=105166536762241': 1,
//     'csv?versionid=105172445630401': 1,
//     'csv?versionid=105166536063873': 1,
//     'csv?versionid=105166536873729': 1,
//     'csv?versionid=105166537019905': 1,
//     'csv?versionid=105172445827521': 1,
//     'csv?versionid=105172445904577': 1,
//     'csv?versionid=105172445805441': 1,
//     'csv?versionid=105166536460033': 1,
//     'csv?versionid=105166536838913': 1,
//     'csv?versionid=105172446089665': 1,
//     'csv?versionid=105166536439937': 1,
//     'csv?versionid=105172445647297': 1,
//     'csv?versionid=105172445552257': 1,
//     'csv?versionid=105166536801793': 1,
//     'csv?versionid=105172445848385': 1,
//     'csv?versionid=105166536679681': 1,
//     'csv?versionid=105166536742465': 1,
//     'csv?versionid=105172446109697': 1,
//     'csv?versionid=105172445966081': 1,
//     'csv?versionid=105172446138241': 1,
//     'csv?versionid=105166536479681': 1,
//     'csv?versionid=105166536641153': 1,
//     'csv?versionid=105172445586433': 1,
//     'csv?versionid=105172446070849': 1,
//     'csv?versionid=105172445884737': 1,
//     'csv?versionid=105166536563777': 1,
//     'csv?versionid=105172445512385': 1,
//     'csv?versionid=105166536659521': 1,
//     'csv?versionid=105166536548481': 1,
//     'csv?versionid=105166536601665': 1,
//     'csv?versionid=105166536621313': 1,
//     'csv?versionid=105172446160001': 1,
//     'csv?versionid=105166536581825': 1,
//     'csv?versionid=105166536704193': 1,
//     'csv?versionid=105166536721409': 1,
//     'csv?versionid=105166540313089': 1,
//     'csv?versionid=105166540406977': 1,
//     'csv?versionid=105166540341569': 1,
//     'csv?versionid=105166540360065': 1,
//     'csv?versionid=105166540385793': 1,
//     'csv?versionid=105166540430145': 1,
//     'csv?versionid=105172445450433': 1,
//     'csv?versionid=105172390577345': 1,
//     'csv?versionid=105172390599553': 1,
//     'csv?versionid=105172390643393': 1,
//     'csv?versionid=105172500341441': 1,
//     'csv?versionid=105172390466305': 1,
//     'csv?versionid=105172500356481': 1,
//     'csv?versionid=105172390555841': 1,
//     'csv?versionid=105172390488769': 1,
//     'csv?versionid=105172500325953': 1,
//     'csv?versionid=105172500286657': 1,
//     totalRows: 596235,
//     valid: 407751
//   }