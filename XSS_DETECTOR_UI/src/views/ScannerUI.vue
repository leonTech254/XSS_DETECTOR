<template>
    <div>
    <div class="page-wrapper">
    <div class="left">
    <div style="width:80%;">
    <div class="ScanInput">
        <input type="text" placeholder="Enter Website URL" v-model="searchInput">
        <span @click="ScanFunc"><i class="search-icon fa-solid  fa-magnifying-glass"></i></span>
    </div>
    </div>
    
    
    
    </div>
    <div class="right">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vitae, doloremque ea? Nulla, veritatis perspiciatis! Distinctio, officiis sapiente! Commodi culpa nostrum quibusdam dolorem, iste rerum saepe fugiat, maiores reiciendis qui voluptate.</div>
    </div>


    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            searchInput: ''
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
.left

{
display: flex;
flex-direction: column;
justify-content: center;
align-items: center;

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


</style>