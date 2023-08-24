import React, { Fragment, useContext, useState } from 'react';
import { Button, Divider, Form, Input } from 'antd';
import { Link } from 'react-router-dom';
import { AuthContext } from '../context/auth/AuthState';

const onFinishFailed = (errorInfo) => {
  console.log('Failed:', errorInfo);
};
const Signup = () => {
  const {registerUser} = useContext(AuthContext)
  const [user, setUser] = useState({username:null, password:null})

  const onFinish = (values) => {
    setUser({username:values.username, password:values.password})
    console.log('Success:', user);
    
    registerUser(user)
  };

  return <Fragment><Divider orientation="left">Sign Up for New User</Divider><br></br><Form
    name="basic"
    labelCol={{
      span: 8,
    }}
    wrapperCol={{
      span: 16,
    }}
    style={{
      maxWidth: 600,
    }}
    initialValues={{
      remember: true,
    }}
    onFinish={onFinish}
    onFinishFailed={onFinishFailed}
    autoComplete="off"
  >
    <Form.Item
      label="Username"
      name="username"
      value={user.username}
      rules={[
        {
          required: true,
          message: 'Please input your username!',
        },
      ]}
    >
      <Input />
    </Form.Item>

    <Form.Item
      label="Password"
      name="password"
      value={user.password}
      rules={[
        {
          required: true,
          message: 'Please input your password!',
        },
      ]}
    >
      <Input.Password />
    </Form.Item>

    <Form.Item
      label="Confirm Password"
      name="passwordconfirm"
      rules={[
        {
          required: true,
          message: 'Please confirm your password!',
        },
        ({ getFieldValue }) => ({
          validator(_, value) {
            if (!value || getFieldValue('password') === value) {
              return Promise.resolve();
            }
            return Promise.reject(new Error('The new password that you entered do not match!'));
          },
        }),
      ]}
    >
      <Input.Password />
    </Form.Item>

    

    <Form.Item
      wrapperCol={{
        offset: 8,
        span: 16,
      }}
    >
      <Button type="primary" htmlType="submit">
        Submit
      </Button>{"  "}<Link to='/login'><Button >Login</Button></Link>
    </Form.Item>
  </Form></Fragment>
};
export default Signup;