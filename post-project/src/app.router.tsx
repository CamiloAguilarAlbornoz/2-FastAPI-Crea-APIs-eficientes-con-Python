import { createBrowserRouter, Navigate } from "react-router";
import { lazy } from "react";
import { HomePage } from "./posts/pages/home/HomePage";
import { PostPage } from "./posts/pages/post/PostPage";
import { DeletePost } from "./posts/pages/message/DeletePost";
import { TagsPage } from "./posts/pages/tags/TagsPage";
import { CreatePost } from "./posts/pages/new_post/CreatePost";

const PostLayout = lazy(() => import('./posts/layouts/PostLayout'))

export const appRouter = createBrowserRouter([
    {
        path: '/',
        element: <PostLayout />,
        children: [
            {
                index: true,
                element: <HomePage />
            },
            {
                path: 'post/:id_post',
                element: <PostPage />
            },
            {
                path: 'post/delete/:id_post',
                element: <DeletePost />
            },
            {
                path: 'navigate-by-tags',
                element: <TagsPage />
            },
            {
                path: 'new',
                element: <CreatePost />
            },
            {
                path: ':id_post/edit',
                element: <CreatePost />
            }
        ]
    },
    {
        path: '*',
        element: <Navigate to='/'/>
    }
])