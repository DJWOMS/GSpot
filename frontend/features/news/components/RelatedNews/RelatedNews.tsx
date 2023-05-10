import Section from 'components/Section'
import NewsItem from '../NewsItem'

const RelatedNews = () => {
  return (
    <Section title="Related news">
      <div className="flex gap-4">
        <div className="w-full">
          <NewsItem
            title={'New hot race from your favorite computer games studio'}
            imageSrc={'https://loremflickr.com/640/400'}
            date={'3 h ago'}
            category={'Overview'}
            size={'normal'}
            commentsCount={2}
            url={'#'}
          />
        </div>

        <div className="w-full">
          <NewsItem
            title={'New hot race from your favorite computer games studio'}
            imageSrc={'https://loremflickr.com/640/400'}
            date={'3 h ago'}
            category={'PC'}
            size={'normal'}
            commentsCount={0}
            url={'#'}
          />
        </div>

        <div className="w-full">
          <NewsItem
            title={'New hot race from your favorite computer games studio'}
            imageSrc={'https://loremflickr.com/640/400'}
            date={'3 h ago'}
            category={'VR'}
            size={'normal'}
            commentsCount={50}
            url={'#'}
          />
        </div>
      </div>
    </Section>
  )
}

export default RelatedNews
