<template>
    <div>
    <div class="page-wrapper">
    <div class="left">
    <div class="leftWrapper" >
    <div style="width:80%;">
    <div class="ScanInput" >
        <input type="text" placeholder="Enter Website URL" v-model="searchInput">
        <span @click="ScanFunc"><i class="search-icon fa-solid  fa-magnifying-glass"></i></span>
    </div>
    </div>
    <div class="response-screen">
    <div class="title">payload tested</div>
    <ul>
    <li v-for="(payload,index) in resposeArray" key="index">
    <span class="label">Vulnerable(payload)</span>==<span class="label-value"> {{ payload.payload }}</span>
   
    
    </li>
    </ul>
    
    
    </div>


    </div>
    </div>
    <div class="right">
    <p>Cross-site scripting (XSS) is a type of security vulnerability that allows attackers to inject malicious scripts into web pages viewed by other users. These scripts can then execute within the victim's browser, potentially allowing the attacker to steal sensitive information, such as login credentials or credit card numbers, or to perform actions on behalf of the victim, such as making unauthorized purchases or sending spam.</p>

    <p>
   <div class="important"> To protect yourself against XSS attacks, it's important to be aware of the risks and to take steps to minimize your exposure. 
        Some best practices include:</div>
    <ul>
    <li>Keeping your web browser and software up to date with the latest security patches and updates.</li>
    <li>Being cautious about clicking on links or downloading attachments from unknown sources.</li>
    <li>Using a reputable antivirus and anti-malware program to protect your computer and devices.</li>
    <li>Enabling security features such as cross-site scripting protection in your web browser.</li>

    <li>Being aware of common signs of an XSS attack, such as unexpected pop-ups or strange behavior on web pages.</li>
    <li>Avoiding inputting personal or sensitive information on untrusted or suspicious websites.</li>
    
    
    
    </ul>

        
        
        
        
        
        
    
    
    </p>
    
    
    </div>
    </div>


    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            searchInput: '',
            resposeArray: []
        }
    },
    
        methods: {
        ScanFunc()
            {
                if (this.searchInput == '')
                {
                    alert("Enter website Url")
                } else
                {
                    let data = { "url": this.searchInput }
                    axios.post("/api/scan_website", data)
                        .then((res) => {
                            let response = res.data.scan_result;
                            this.resposeArray = response;
                            

                            
                        })
                        .catch((err) => {


                            
                        })
                    
                    

                }
                

            
        }
        },
        
    }
</script>

<style scoped>
.page-wrapper
{
    display: grid;
    grid-template-columns:repeat(2,1fr);
    gap: 2rem;
}
.leftWrapper

{
display: flex;
flex-direction: column;
justify-content: center;
align-items: center;
width: 80%;

}
.ScanInput
{
    background-color: white;
    width: 100%;
    border: 1px solid orange;
    color: black;
    border-radius: .5rem;

    display: flex;
    justify-content: space-around;
    align-items: center;
    

}
.ScanInput input
{
    padding: 10px;
    width: 90%;
    background:none;
    border: none;
    font-weight: bold;
    color: black;
}
.ScanInput input:focus
{
    border: none;
    outline: none;
}
.search-icon
{
    font-size: 1.5rem;
    color: green;
    border-left: 2px solid green;
    padding: 8px;
    cursor: pointer;

}
.search-icon:active
{
    transform: scale(.9);

}
.important
{
    color: red;
    font-style: italic;
    font-weight: bold;
}
.response-screen
{
    height: 20rem;
    overflow: auto;
    border: 2px solid green;
    width: 100%;
    margin-top: 2rem;





}
.response-screen .title
{
    text-align: center;
    text-transform: uppercase;
    color: white;
    font-weight: bold;
}
.response-screen .label
{
    color: red;
}

.label-value
{
    color: aqua;
}
</style>