//Client side javascript code can go here

async function test_async_ping() {
    const json_client_vars = JSON.stringify({
        client_var: 'Hi, from client!'
    });
    const res = await fetch("http://127.0.0.1:5000/hello", {
        method: "POST",
        headers: new Headers({ "content-type": "application/json" }),
        body: json_client_vars,
    });
    const data_json = await res.json();
    console.log("Async response: ", data_json);
};