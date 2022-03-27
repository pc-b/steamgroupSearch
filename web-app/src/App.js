import './App.css';
import JSONDATA from './py/groups.json'
import{useState} from 'react'
import React from 'react';

function App() 
{  
  const [searchTerm, setSearchTerm] = useState('');

  function handleChange() {
    if (document.getElementById("public").checked === true) {
      console.log("checked")
      return true
    }
    else {
      console.log("unchecked")
      return false
    }
  }


  
  return (
  <div className="App">
    <p class="info">Pink text is group name, click to go to steam page</p>
    <input type="text" class="search" placeholder="Search..." onChange={event => {setSearchTerm(event.target.value)}}/>
    <input type="checkbox"  id="public" class="public" name="box" onChange={handleChange}/>
    <label for="public">Public?</label>


    
    {JSONDATA.filter((val)=>
    {
      if (searchTerm !== "") {
        if (val.GroupTag.toLowerCase().substring(0, searchTerm.length).match(searchTerm))  
      { /* and check if box ix checked */
        return val
      }
      }
    }
    ).map((val, key)=> 
    {
      return <div>
        <a href={val.GroupURL}>{val.GroupName}</a> {val.GroupTag} {val.IsPrivate}
        </div>
    })}
    <header className="App-header"></header>

    
    
  </div>
  );
}



export default App;
