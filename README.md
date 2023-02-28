# XSS_DETECTOR

This is a simple web application built using Python Flask and Vue.js that allows users to test for XSS vulnerabilities on websites. The tool works by sending a series of POST requests with different XSS payloads to a specified URL, and then checking the response HTML for any signs that the payloads were executed.

## INSTALLATION

To install and run the tool, follow these steps:

<li>Clone the repository to your local machine:</li>
<pre>
<code>
git clone git@github.com:leonTech254/XSS_DETECTOR.git
</code>
</pre>
<li>Install the reqirements</li>
<pre>
<code>pip install -r requirements.txt
</code>
</pre>
<li>Install the required Node.js packages using npm</li>
<pre>
<code>
cd XSS_DETECTOR_UI
npm install
</code>
</pre>

## INSTALLATION

<li>Start the Flask server</li>
<pre>
<code>python app.py
</code>
</pre>
<li>Start the Fronted</li>
<p>While in the XSS_DETECTOR_UI run</p>
<pre>
<code>npm run dev
</code>
</pre>

## TEST CASES

<li>
    DVWA: http://localhost/HACKLAB/DVWA/vulnerabilities/xss_r/ <br>
</li>
<li>Mutillidae: http://localhost/mutillidae/index.php?page=user-info.php</li>

### SCREENSHOTS

<li>landing page</li>

<img src="https://github.com/leonTech254/XSS_DETECTOR/blob/main/Images/landingPage.png?raw=true"  title="landing page"/>
<li>IMPLEMENTATION</li>
<img src="https://github.com/leonTech254/XSS_DETECTOR/blob/main/Images/toolImplementation.png?raw=true"  title="implementation"/>

# DEVELOPERS

<li>BACKED& FRONTED: martinleontech23@gmail.com </li>
<li>FRONTED:  wanguivalentine19@gmail.com</li>
