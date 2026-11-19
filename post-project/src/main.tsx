import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import {PostApp} from './PostApp.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <PostApp />
  </StrictMode>,
)
