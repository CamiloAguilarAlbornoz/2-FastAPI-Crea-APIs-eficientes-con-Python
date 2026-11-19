import { CustomHeader } from '../../../components/custom/CustomHeader';
import { CustomFooter } from '../../../components/custom/CustomFooter';
import { CustomJumbotron } from '../../components/CustomJumbotron';
import { PostCardList } from '../../components/PostCardList';
import { CustomPaginated } from '../../components/CustomPaginated';
import { usePosts } from '../../hooks/usePosts';
import { Toaster } from 'sonner';
import { CustomTitle } from '../../components/CustomTitle';
import { CustomFullScreenLoading } from '../../../components/custom/CustomFullScreenLoading';

export const HomePage = () => {

  const {getAllByTextOrDefault} = usePosts()
  const {data, isLoading} = getAllByTextOrDefault()

  return (
    <>
      <Toaster theme='dark'/>
      <CustomHeader />
      
      <div className="mx-auto max-w-6xl px-4 py-10 sm:px-6">
        
        <CustomTitle />
        <CustomJumbotron />

        <div className='mt-10 flex flex-col gap-8 lg:flex-row'>
          {
            isLoading && (<CustomFullScreenLoading />)
          }
          <PostCardList pagePosts={data?.items || []} />
        </div>

        <CustomPaginated
        totalPages = {data?.total_pages || 0}
        hasPrev = {data?.has_prev || false}
        hasNext = {data?.has_next || false}
        />
        
      </div>

      <CustomFooter />
    </>
  );
}
