import { RouterProvider } from "react-router"
import { appRouter } from "./app.router"
import { QueryClient, QueryClientProvider } from "@tanstack/react-query"
import { ReactQueryDevtools } from "@tanstack/react-query-devtools"

const queryClient = new QueryClient()

export const PostApp = () => {

  return (
    <QueryClientProvider client = {queryClient}>
      <RouterProvider router = {appRouter} />
      <ReactQueryDevtools initialIsOpen = {false} />
    </QueryClientProvider>
  )
}
