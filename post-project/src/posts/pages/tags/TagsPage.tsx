import { CustomHeader } from '../../../components/custom/CustomHeader';
import { CustomFooter } from '../../../components/custom/CustomFooter';
import { PostCardList } from '../../components/PostCardList';
import { usePosts } from '../../hooks/usePosts';
import { Toaster } from 'sonner';
import { AllTagsList } from '../../components/AllTagsList';
import { CustomTitle } from '../../components/CustomTitle';

export const TagsPage = () => {

  const {getPostByTags} = usePosts()
  const {data : posts} = getPostByTags()
  
  return (
    <>
      <Toaster theme='dark'/>
      <CustomHeader />
      
      <div className="mx-auto max-w-6xl px-4 py-10 sm:px-6">
        
        <CustomTitle />

        <div className='mt-10 flex flex-col gap-8 lg:flex-row'>
          <PostCardList pagePosts={posts || []} />
          <AllTagsList />
        </div>
        
      </div>

      <CustomFooter />
    </>
  );
}
