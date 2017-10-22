import React, { Component } from 'react';

export default class LoginForm extends Component {
  constructor(props) {
    super(props);

    this.state = {
      email: '',
      password: ''
    };

    this.onSubmit = this.onSubmit.bind(this);
  }

  makeHandleChange(field) {
    return (e) => {
      this.setState({ [field]: e.target.value });
    }
  }

  onSubmit(e) {
    e.preventDefault();

    const { email, password } = this.state;

    this.props.onSubmit(email, password);
  }

  render() {
    return (
      <form onSubmit={this.onSubmit}>
        <label htmlFor='email'>Email</label>
        <input
          type='text'
          name='email'
          placeholder='email'
          onChange={this.makeHandleChange('email')} />

        <label htmlFor='password'>Password</label>
        <input
          type='password'
          name='password'
          placeholder='password'
          onChange={this.makeHandleChange('password')} />

        <button type='submit'>Submit</button>
      </form>
    );
  }
}
