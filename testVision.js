var key = process.env["GOOGLE_KEY"];
var image = process.env["GOOGLE_IMAGE"];

var fs = require('fs');
var data = fs.readFileSync(image, {encoding: "base64"});

var request = require("request");

var r = {
    "requests": {
        "image" : {
            "content": data
        },
        "features": [
            {
                "type" : "TEXT_DETECTION"
            }],
        "imageContext": {
                "languageHints": ["ru"] 
        }
    }
};

var opts = {
    url: "https://vision.googleapis.com/v1/images:annotate?key=" + key,
    method: "POST",
    body: JSON.stringify(r)
};

request(opts, (err,res,body) => {
    console.log(err);
    console.log(body);
});
