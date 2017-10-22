import React, { Component } from 'react';
import Sound from 'react-sound';

export default class PlaySong extends Component {
  constructor(props) {
    super(props);

    this.state = {
      songId: '',
      url: ''
    };

    this.onChange = this.onChange.bind(this);
    this.onClick = this.onClick.bind(this);
  }

  componentDidMount() {
    const { socket } = this.props;

    socket.on('stream_url:received', (url) => {
      this.setState({ url });
    });
  }

  onChange(e) {
    this.setState({ songId: e.target.value });
  }

  onClick() {
    const { socket } = this.props;
    const { songId } = this.state;

    socket.emit('stream_url:request', songId);
  }

  render() {
    const { url, songId } = this.state;

    return (
      <div>
        <p>Example song ID: cfce177b-a50e-379e-897f-a5f056f2f0de</p>
        <input type='text' name='songId' placeholder='Song ID' onChange={this.onChange} value={songId} />
        <button type='button' onClick={this.onClick}>Submit</button>

        { url &&
          <Sound
            url={url}
            playStatus={Sound.status.PLAYING} /> }

      </div>
    );
  }
}
