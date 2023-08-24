import React, { Fragment , useContext, useState} from 'react'
import { List, Button, Empty } from 'antd'
import {DeleteOutlined} from '@ant-design/icons'
import { AuthContext } from '../context/auth/AuthState'
  

  
const UploadedList = () => {
  const {user,token} = useContext(AuthContext)
  const [list, setList] = useState([
    {
        "url": "URL object (f2210faf-9780-4f24-a1c3-4343c4f67b8a)",
        "owner": "abc",
        "file": "uploads/f2210faf-9780-4f24-a1c3-4343c4f67b8a.docx",
        "filename": "Cover Letter.docx",
        "date":"date"
    },
    {
        "url": "URL object (d2e5a502-eeaa-44ee-927d-e45344b0cea6)",
        "owner": "abc",
        "file": "uploads/d2e5a502-eeaa-44ee-927d-e45344b0cea6.docx",
        "filename": "Cover Letter.docx",
        "date":"date"}
])
  const onclick = (e)=>{
    console.log(e.target.value.slice(12,48))
    
  }
  return ( 
    <List
      header={<div>Previosly Uploaded Files</div>}
 
      bordered
      dataSource={list}
      renderItem={(item,key) => (
        <Fragment>{list.length ? <List.Item actions={[<Button value ={item.url} onClick={onclick} danger icon={<DeleteOutlined onClick={e=> e.stopPropagation() }/>}></Button> ]}>
       <List.Item.Meta
         
          title={item.filename}
          description={item.file+' | '+item.date}
        /> 
        </List.Item> : <Empty image={Empty.PRESENTED_IMAGE_SIMPLE} />}</Fragment>
      )}
    />
  )
}

export default UploadedList