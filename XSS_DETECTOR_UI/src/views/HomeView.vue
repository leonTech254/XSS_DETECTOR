<script setup>

</script>

<template>
<div class="page-wrapper">

<div class="banner">
<h1 class="title">Welcome To our XSS Scanner Tool</h1>
<h3 class="content">
Thanks for visiting our website! We're here to educate you about XSS attacks and provide you with the knowledge and
tools you need to prevent them from happening

</h3>
<div>
<button class="lbtn">test website</button>

</div>

</div>


</div>






</template>
<style scoped>
.page-wrapper
{
background-color: red;
width: 100%;
height: 100vh;
background: linear-gradient(rgba(0, 0, 0, 0.725),black),url("../assets/Images/imagebg.jpg");

background-position: center;
background-repeat: no-repeat;
background-size: cover;

display: flex;
flex-direction: column;
justify-content: center;
align-items: center;

}
.banner
{
  padding: 5rem;
  text-align: center;
  margin-left: 1rem;
  margin-right: 1rem;
}
.banner .title
{
  font-weight: bolder;

}
.lbtn:active
{
  transform: scale(.9);
}
.lbtn
{
  padding: 10px;
  padding-left: 15px;
  padding-right: 15px;
  text-transform: uppercase;
  background: none;
  color: white;
  font-weight: bold;
  border: 1px solid green;
  margin-top: 2rem;
  cursor: pointer;
  
}
@media (min-width:600px) {
  .banner .title {
      font-weight: bolder;
      font-size: 3.5em;
  
    }
    .banner {
      padding: 1rem;
      text-align: center;
      margin-left: 7rem;
      margin-right: 7rem;
      font-size: larger;
    }
  
}
</style>