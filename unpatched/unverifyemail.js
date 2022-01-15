const {default:axios} = require("axios")
let token = process.argv[2]
if (!token || token === "") {
    throw console.error(`node ${__filename} <token>`)
}
axios({
    method: "get",
    url: "https://discord.com/api/guilds/0/members",
    headers: {
        authorization: token
    }
}).catch((err) => {
    console.log("Email unverified!")
})
// It will literally send an email like "Thanks for registering an account" when you re-verify your email
