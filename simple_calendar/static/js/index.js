//var React = require('react')
//var ReactDOM = require('react-dom')
import React from 'react'
import ReactDOM from 'react-dom'
import Fetch from 'react-fetch'
import createReactClass from 'create-react-class'

var Hello = createReactClass({
    render: function() {
        return (
            <div>
                <h1> Appointment Calendar </h1>
                <Fetch url="http://127.0.0.1:8000/rest_appointment">
                    <TestComponent/>
                </Fetch>
            </div>
        )
    }
})

class TestComponent extends React.Component {
  render() {
    for (let i = 0; i < Object.keys(this.props).length; i++) {
        console.log(this.props[0][i])
        <span>this.props[0][i]</span>
    }
    return <div/>
  }
}

ReactDOM.render(<Hello />, document.getElementById('container'))