import React, {useState,useContext} from 'react';
import { Button, Divider, Form, Input } from 'antd';
import { AuthContext } from '../context/auth/AuthState';
import { Link } from 'react-router-dom';


const onFinishFailed = (errorInfo) => {
  console.log('Failed:', errorInfo);
};
const Login = () => {
  const [user, setUser] = useState({username:null, password:null});
  const { loginUser } = useContext(AuthContext);

  const onFinish = (values) => {

    setUser({username:values.username, password:values.password})
    console.log(user)
    loginUser(user);
  };

  return(<Form
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
   
    onFinish={onFinish}
    onFinishFailed={onFinishFailed}
    autoComplete="off"
  ><Divider orientation="left">User Login</Divider><br></br>
    <Form.Item
      label="Username"
      name="username"
      rules={[
        {
          required: true,
          message: 'Username cannot be blank!',
        },
      ]}
    >
      <Input />
    </Form.Item>

    <Form.Item
      label="Password"
      value={user.password}
      name="password"
      rules={[
        {
          required: true,
          message: 'Password cannot be blank!',
        },
      ]}
    >
      <Input.Password />
    </Form.Item>
    <Form.Item
     wrapperCol={{
   offset:8,
      span: 16,
    }}
    >
      <Button type="primary" htmlType="submit">
        {"   "}Submit {"    "}
      </Button> <Link to='/signup'><Button >Sign Up</Button></Link>
    </Form.Item>
  </Form>
)};
export default Login;