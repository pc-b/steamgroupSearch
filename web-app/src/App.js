import './App.css';
import JSONDATA from './py/groups.json'
import{useState} from 'react'
function App() 
{
  const [searchTerm, setSearchTerm] = useState('');
  return (
  <div className="App">
    <input type="text" placeholder="Search..." onChange={event => {setSearchTerm(event.target.value)}}/>
    <input type="checkbox" id="public" name="public" value="yes"/>
    <label for="public">Public</label>

    
    {JSONDATA.filter((val)=>
    {
      if (searchTerm == "")
      {
        return val
      }
      else if (val.tag.toLowerCase().includes(searchTerm.toLowerCase()))  
      { /* and check if box ix checked */
        return val
      }

    }
    ).map((val, key)=> 
    {
      return <div>
        {val.GroupName} {val.GroupTag} {val.GroupURL} {val.IsPrivate}
        </div>
    })}
    <header className="App-header"></header>

    
    
  </div>
  );
}

function checkBox() 
{
  var chkBox = document.getElementById('public');
  if (chkBox.checked)
  {
    return true;
  }
}

export default App;
