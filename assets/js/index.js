//var React = require('react')
//var ReactDOM = require('react-dom')
import React from 'react'
import ReactDOM from 'react-dom'
import Fetch from 'react-fetch'
import createReactClass from 'create-react-class'

var AptCalendar = createReactClass({
    getInitialState: function(){
    return {
       data: {
          apts: [] 
       }
    };
    },
    render: function() {
        return (
            <div>
                <h1> Appointment Calendar </h1>
                <Fetch url="http://127.0.0.1:8000/rest_appointment">
                    <AptComponent data={this.state.data}/>
                </Fetch>
            </div>
        )
    }
})

class AptComponent extends React.Component {
    render() {
        return (
            <p className="AptComponent">
            {
                this.props.data.apts.map(function(apt) {
                    return <li key={apt}>{apt}</li>
                })
            }
            </p>
        )
    }
}

ReactDOM.render(<AptCalendar />, document.getElementById('container'))