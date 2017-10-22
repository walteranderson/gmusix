import React, { Component } from 'react';
import io from 'socket.io-client';
import LoginForm from './LoginForm';
import PlaySong from './PlaySong';

const socket = io('http://localhost:5000');

export default class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      loggedIn: false
    };
  }

  componentDidMount() {
    socket.emit('auth:check');

    socket.on('auth:result', (loggedIn) => {
      console.log('auth:result', loggedIn);

      this.setState({ loggedIn });
    });
  }

  onSubmit(email, password) {
    socket.emit('auth:login', { email, password });
  }

  render() {
    const { loggedIn } = this.state;

    // Not Authenticated
    if (!loggedIn) {
      return (
        <LoginForm onSubmit={this.onSubmit} />
      );
    }

    // Authenticated
    return (
      <div>
        <p>Logged In</p>
        <PlaySong socket={socket} />
      </div>
    );
  }
}
