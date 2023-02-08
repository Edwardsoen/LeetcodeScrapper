<h1> Leetcode Scrapper </h1> 
LeetCode Scraper is a Selenium based Python script that scrapes information from Leetcode.com and stores the data in JSON format.
<br>
<br>



>  Note: if you just want to see company wise problems check out the subtree <a href = "https://github.com/Edwardsoen/LeetcodeScrapper/tree/company-wise-data"> here </a>, it is scraped in Febuary 2023. Alternatively you can checkout <a href = "https://github.com/Edwardsoen/Leetcode-Premium-Unlocker"> Leetcode Premium Unlocker </a> browser extension, which will automatically inject premium data when you open the website. 

<h2> Dependencies  </h2>  

```
selenium==4.8.0
```



<h2> Currently Supported pages </h2>
<li> https://leetcode.com/problemset/* </li>
<li>https://leetcode.com/problem-list/* </li>
<li>https://leetcode.com/company/ </li>


<h2> Usage </h2>  


clone repo + install dependencies

```
git clone https://github.com/Edwardsoen/LeetcodeScrapper.git
cd LeetcodeScrapper 
pip install -r requirements.txt
```

download chromedriver <a href = "https://chromedriver.chromium.org/downloads"> here  </a> and paste it to system path


if you want to scrape single page, simply run
```
Python3 main.py {url}  
```
but in most cases you probably want to scrape multiple pages, in which case you need to store the urls into seperate txt file (or you can use pre-scrapped urls <a href ="https://github.com/Edwardsoen/LeetcodeScrapper/tree/master/urls"> here</a>) and pass it like this
```
Python3 main.py {urlsfile.txt}
```
if you need to scrape premium data you can pass username and password like so 
```
Python3 main.py -u {username} -p {password} {urls}  
```


<h2> Sample output </h2>

<h3> Company Problem page <h3> 

```

{
  "data": [
    {
      "duration": "All time",
      "problemData": [
        {
          "acceptance": "73.6%",
          "difficulty": "Medium",
          "frequency": 0,
          "problemId": "2020",
          "problemName": "Number of Accounts That Did Not Stream",
          "url": "https://leetcode.com/problems/number-of-accounts-that-did-not-stream"
        }
      ]
    },
    {
      "duration": "All time",
      "problemData": [
        {
          "acceptance": "52.0%",
          "difficulty": "Medium",
          "frequency": 0,
          "problemId": "1990",
          "problemName": "Count the Number of Experiments",
          "url": "https://leetcode.com/problems/count-the-number-of-experiments"
        }
      ]
    },
    {
      "duration": "All time",
      "problemData": [
        {
          "acceptance": "72.7%",
          "difficulty": "Medium",
          "frequency": 0,
          "problemId": "1951",
          "problemName": "All the Pairs With the Maximum Number of Common Followers",
          "url": "https://leetcode.com/problems/all-the-pairs-with-the-maximum-number-of-common-followers"
        }
      ]
    }
  ],
  "companyName": [
    "instagram"
  ]
}

```


<h3> Front page <h3> 

```
{
  "tableData": [
    {
      "isPremium": false,
      "problemName": "2551. Put Marbles in Bags",
      "haveSolution": false,
      "isVideoSolution": false,
      "acceptance": "51.5%",
      "difficulty": "Hard",
      "frequency": "10.7001%",
      "url": "https://leetcode.com/problems/put-marbles-in-bags/"
    },
    {
      "isPremium": false,
      "problemName": "2552. Count Increasing Quadruplets",
      "haveSolution": false,
      "isVideoSolution": false,
      "acceptance": "31.5%",
      "difficulty": "Hard",
      "frequency": "7.09464%",
      "url": "https://leetcode.com/problems/count-increasing-quadruplets/"
    },
    {
      "isPremium": false,
      "problemName": "2553. Separate the Digits in an Array",
      "haveSolution": false,
      "isVideoSolution": false,
      "acceptance": "78.1%",
      "difficulty": "Easy",
      "frequency": "0%",
      "url": "https://leetcode.com/problems/separate-the-digits-in-an-array/"
    },
    {
      "isPremium": false,
      "problemName": "2554. Maximum Number of Integers to Choose From a Range I",
      "haveSolution": false,
      "isVideoSolution": false,
      "acceptance": "50.3%",
      "difficulty": "Medium",
      "frequency": "0%",
      "url": "https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/"
    },
    {
      "isPremium": false,
      "problemName": "2555. Maximize Win From Two Segments",
      "haveSolution": false,
      "isVideoSolution": false,
      "acceptance": "22.8%",
      "difficulty": "Medium",
      "frequency": "0.166546%",
      "url": "https://leetcode.com/problems/maximize-win-from-two-segments/"
    },
    {
      "isPremium": false,
      "problemName": "2556. Disconnect Path in a Binary Matrix by at Most One Flip",
      "haveSolution": false,
      "isVideoSolution": false,
      "acceptance": "21.5%",
      "difficulty": "Medium",
      "frequency": "0%",
      "url": "https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/"
    },
    {
      "isPremium": false,
      "problemName": "2557. Maximum Number of Integers to Choose From a Range II",
      "haveSolution": false,
      "isVideoSolution": false,
      "acceptance": "49.4%",
      "difficulty": "Medium",
      "frequency": "0%",
      "url": "https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-ii/"
    },
    {
      "isPremium": false,
      "problemName": "2558. Take Gifts From the Richest Pile",
      "haveSolution": false,
      "isVideoSolution": false,
      "acceptance": "63.6%",
      "difficulty": "Easy",
      "frequency": "0%",
      "url": "https://leetcode.com/problems/take-gifts-from-the-richest-pile/"
    },
    {
      "isPremium": false,
      "problemName": "2559. Count Vowel Strings in Ranges",
      "haveSolution": false,
      "isVideoSolution": false,
      "acceptance": "47.9%",
      "difficulty": "Medium",
      "frequency": "0%",
      "url": "https://leetcode.com/problems/count-vowel-strings-in-ranges/"
    },
    {
      "isPremium": false,
      "problemName": "2560. House Robber IV",
      "haveSolution": false,
      "isVideoSolution": false,
      "acceptance": "27.1%",
      "difficulty": "Medium",
      "frequency": "0%",
      "url": "https://leetcode.com/problems/house-robber-iv/"
    },
    {
      "isPremium": false,
      "problemName": "2561. Rearranging Fruits",
      "haveSolution": false,
      "isVideoSolution": false,
      "acceptance": "25.6%",
      "difficulty": "Hard",
      "frequency": "0%",
      "url": "https://leetcode.com/problems/rearranging-fruits/"
    }
  ],
  "page": "52"
}

```


<h3> Problem page <h3>

```
{
  "tags": [
    {
      "duration": "1 year - 2 years",
      "companies": [
        [
          "1 year - 2 years",
          "Amazon"
        ]
      ]
    }
  ],
  "problem": "<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> and a positive integer <code>k</code>.</p>\n\n<p>We call an index <code>i</code> <strong>k-big</strong> if the following conditions are satisfied:</p>\n\n<ul>\n\t<li>There exist at least <code>k</code> different indices <code>idx1</code> such that <code>idx1 &lt; i</code> and <code>nums[idx1] &lt; nums[i]</code>.</li>\n\t<li>There exist at least <code>k</code> different indices <code>idx2</code> such that <code>idx2 &gt; i</code> and <code>nums[idx2] &lt; nums[i]</code>.</li>\n</ul>\n\n<p>Return <em>the number of k-big indices</em>.</p>\n\n<p>&nbsp;</p>\n<p><strong class=\"example\">Example 1:</strong></p>\n\n<pre><strong>Input:</strong> nums = [2,3,6,5,2,3], k = 2\n<strong>Output:</strong> 2\n<strong>Explanation:</strong> There are only two 2-big indices in nums:\n- i = 2 --&gt; There are two valid idx1: 0 and 1. There are three valid idx2: 2, 3, and 4.\n- i = 3 --&gt; There are two valid idx1: 0 and 1. There are two valid idx2: 3 and 4.\n</pre>\n\n<p><strong class=\"example\">Example 2:</strong></p>\n\n<pre><strong>Input:</strong> nums = [1,1,1], k = 3\n<strong>Output:</strong> 0\n<strong>Explanation:</strong> There are no 3-big indices in nums.\n</pre>\n\n<p>&nbsp;</p>\n<p><strong>Constraints:</strong></p>\n\n<ul>\n\t<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>\n\t<li><code>1 &lt;= nums[i], k &lt;= nums.length</code></li>\n</ul>\n",
  "relatedTopics": [
    "Array",
    "Binary Search",
    "Divide and Conquer",
    "Binary Indexed Tree",
    "Segment Tree",
    "Merge Sort",
    "Ordered Set"
  ],
  "similarQuestions": [
    {
      "questionName": "Count of Smaller Numbers After Self",
      "difficulty": "Hard"
    },
    {
      "questionName": "Find All Good Indices",
      "difficulty": "Medium"
    }
  ],
  "problemName": "count-the-number-of-k-big-indices"
}
```

<h2> Contributions </h2>
If you have premium account and want to 'donate' data, feel free to open merge request (remember to force add the output folder, it is git-ignored by default). 


