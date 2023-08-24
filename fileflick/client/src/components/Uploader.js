import React, { Fragment, useState } from 'react';
import {CopyToClipboard} from 'react-copy-to-clipboard';
import FileUploader from './FileUploader';
import { Tooltip, Input } from 'antd';
import {CopyOutlined, CheckOutlined} from '@ant-design/icons';


const Uploader = () => {
    const [url, setUrl] =useState({value:"upload a file to display url", copied: false, tooltip:"Copy to Clipboard", color:null});
  return <div style={{padding:'1em'}}><FileUploader /><br></br>
  <div> <Input  
  readOnly 
  addonAfter={<Tooltip placement="top" color={url.color} title={url.tooltip}><CopyToClipboard text={url.value} onCopy={(val) => setUrl({value:url.value, copied: true, color:"green",tooltip:"Copied!"})}>
        {url.copied ? <CheckOutlined /> : 
        <CopyOutlined />}
        </CopyToClipboard></Tooltip>} 
        defaultValue={url.value}/>
       
      </div>
      </div>
};
export default Uploader;