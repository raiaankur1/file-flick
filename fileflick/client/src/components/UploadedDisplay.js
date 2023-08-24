import React , {useContext} from 'react'
import LogInMessage from './LogInMessage';
import UploadedList from './UploadedList';
import { AuthContext } from '../context/auth/AuthState';
const UploadedDisplay = () => {
    const {isAuthenticated} = useContext(AuthContext);
  return (
    <div style={{padding:'1em'}}>{isAuthenticated ? <UploadedList /> : <LogInMessage />}</div>
  )
};

export default UploadedDisplay;