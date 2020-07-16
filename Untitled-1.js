url = "/api/rent_info/query"

fetch(url,{method:"POST",body:JSON.stringify({
    user_id:"xianbei",
    area:"beijing",
    price:200,
    is_out:1,
    min_date:{
        year:"2020",month:"12",day:"4"
    },
    max_date:{
        year:"2020",month:"12",day:"4"
    },
    })})
.then((res) => res.json())
.then((data) => {console.log(data)})

url = "/api/com_user/query"

fetch(url,{method:"POST",body:JSON.stringify({
    user_id:"497e468a0b3bd7a9d65a0952ec1fd261"
})})
.then((res) => res.json())
.then((data) => {console.log(data)})

url = "/api/org_user/add"

fetch(url,{method:"POST",body:JSON.stringify({
    user_name:"gongsi1",
    represent:"xiaoming"
})})
.then((res) => res.json())
.then((data) => {console.log(data)})

url = "/api/org_user/query"

fetch(url,{method:"POST",body:JSON.stringify({
    user_id:"1d485ac7f3458f060801989c7a7b9f90"
})})
.then((res) => res.json())
.then((data) => {console.log(data)})

url = "/api/org_user_pend/add"

fetch(url,{method:"POST",body:JSON.stringify({
    user_name:"gongsi1",
    represent:"xiaoming"
})})
.then((res) => res.json())
.then((data) => {console.log(data)})

url = "/api/org_user_pend/query"

fetch(url,{method:"POST",body:JSON.stringify({
    user_id:"9389aadeb2078320d8dbf53b0558dc84"
})})
.then((res) => res.json())
.then((data) => {console.log(data)})


url = "/api/org_user_pend/delete"

fetch(url,{method:"POST",body:JSON.stringify({
    user_id:"9389aadeb2078320d8dbf53b0558dc84"
})})
.then((res) => res.json())
.then((data) => {console.log(data)})