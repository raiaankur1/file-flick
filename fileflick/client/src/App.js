import React, { Fragment, useState } from 'react';
import { Breadcrumb, Layout, Avatar, theme } from 'antd';
import { Routes, Route, Link } from "react-router-dom";
import {AuthProvider} from './context/auth/AuthState'
import Home from './pages/Home';
import Login from './pages/Login';
import Signup from './pages/Signup';
import NotFound from './pages/NotFound';
import Headerr from './components/Headerr';
const { Content, Footer } = Layout;

const App = () => {
  const {
    token: { colorBgContainer },
  } = theme.useToken();
 
  return (
    <Layout className="layout">
      <Headerr />
      <Content
        style={{
          padding: '50px',
        }}
      >
       
        <div
          className="site-layout-content"
          style={{
            background: colorBgContainer,
            padding:'2em'
          }}
        >
          <AuthProvider>
            <Routes>
            <Route exact path="/" element={<Home/>} />
            <Route path="/login" element={<Login />} />
            <Route path="/signup" element={<Signup />} /> 
            <Route path="/*" element={<NotFound />} />
          </Routes>
        </AuthProvider>
        </div>
      </Content>
      <Footer
        style={{
          textAlign: 'center',
        }}
      >
        Ant Design ©2023 Created by Ant UED
      </Footer>
    </Layout>
  );
};
export default App;