// import React, { Component } from 'react'; // new
import React, { Component } from 'react'; //nuevo
import ReactDOM from 'react-dom';
import axios from 'axios'; //nuevo
import UsersList from './components/UsersList';
import AddUser from './components/AddUser';

//nuevo
class App extends Component {
  //new
  constructor() {
    super();
    //nuevo
    this.state ={
      users: [],
      username: '',
      email: '',
    };
    this.addUser = this.addUser.bind(this);
    this.handleChange = this.handleChange.bind(this);
  };
  //nuevo
  componentDidMount() {
    this.getUsers();
  };

  //nuevo
  getUsers() {
    axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
    .then((res) => { this.setState({ users: res.data.data.users}); })
    .catch((err) => {console.log(err); });
  }
  render(){
    return(
        <section className='section'>
          <div className='container'>
            <div className='columns'>
              <div className='column is-half'>
                <br/>
                <h1 className='title is-1'>Todos los usuarios</h1>
                <hr/><br/>
                <AddUser addUser={this.addUser}/>
                <br/><br/>
                {/*new*/}
                <UsersList users={this.state.users}/>
             </div>
            </div>
          </div>
        </section>
    )
  }
  addUser(event) {
    event.preventDefault();
    console.log('comprobación de validez!');
    console.log(this.state);
  };

  handleChange(event) {
    const obj = {};
    obj[event.target.name] = event.target.value;
    this.setState(obj);
  };

};

ReactDOM.render(<App />, document.getElementById('root'));
