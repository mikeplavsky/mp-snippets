var config = {
    projectId: "dauntless-tube-104117",
    keyFilename: "./keyfile.json"
};

var gcloud = require("gcloud")(config);
var vision = gcloud.vision();

if (process.argv.length != 3) {

    console.log("Need picture!");
    process.exit(1);

}

var opts = {
};

vision.detectText(process.argv[2], opts, (err,txt)=>{

    console.log(err)
    console.log(txt)

});
