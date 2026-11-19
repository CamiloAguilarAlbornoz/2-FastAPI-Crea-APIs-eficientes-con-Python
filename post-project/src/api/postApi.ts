import axios from "axios";

const postApi = axios.create({
    baseURL: import.meta.env.VITE_API_URL,
})

export {postApi}
