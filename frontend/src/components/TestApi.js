import React, { useEffect, useState } from 'react';


function TestAPI() {

    const [syncMsg, setSyncMsg] = useState();
    const [asyncMsg, setAsyncMsg] = useState();

    function test_sync_ping() {
        fetch('http://127.0.0.1:5000/hello')
        .then(r =>  r.json().then(data => ({status: r.status, body: data})))
        .then(obj => {
        console.log("Sync response: ", obj);
        console.log(obj.status);
        setSyncMsg(obj.body.message);
        });
    };

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
        setAsyncMsg(data_json.message);
    };


    useEffect(() => {
        console.log("useEffect fired from TestAPI!");
        test_sync_ping();
        test_async_ping();
    }, []);


  return (
    <div>
        <h5>Synchronous response from server ping test: {syncMsg}</h5>
        <h5>Aynchronous response from server ping test: {asyncMsg}</h5>
    </div>
  );
}

export default TestAPI;