import React from 'react'
import { Button, Result } from 'antd';
import { Link } from 'react-router-dom';

const LogInMessage = () => {
  return (
    <Result
    status="error"
    title="You are not Logged In!"
    subTitle="Please Login to keep track of Uploaded Files"
    extra={[
      <Link to='/login'><Button type="primary" key="console">
        Go to Login Page
      </Button></Link>,
      
    ]}
  />
  )
}

export default LogInMessage;