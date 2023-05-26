import Section from 'components/Section'
import { NewsItem } from 'features/news/components'
import s from './LatestNews.module.css'

const LatestNews = () => {
  return (
    <Section title="Latest news">
      <div className={s.latestWrap}>
        <div className={s.latestNews}>
          <NewsItem
            title={'New hot race from your favorite computer games studio'}
            imageSrc={'https://loremflickr.com/640/400'}
            date={'3 h ago'}
            category={'NFS'}
            size={'big'}
            commentsCount={3}
            url={'#'}
          />
        </div>

        <div className={s.latestNews}>
          <NewsItem
            title={'New hot race from your favorite computer games studio'}
            imageSrc={'https://loremflickr.com/640/400'}
            date={'3 h ago'}
            category={'CS:GO'}
            size={'big'}
            commentsCount={10}
            url={'#'}
          />
        </div>

        <div className={s.latestNews}>
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

        <div className={s.latestNews}>
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

        <div className={s.latestNews}>
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

export default LatestNews
