import { FC } from 'react'
import Section from 'components/Section'
import { NewsItem } from 'features/news/components'
import s from './page.module.css'

const NewsPage: FC = () => {
  return (
    <Section title="Новости">
      <section className="section section--last section--catalog">
        <div className={s.sort}>
          <div className={s.filterWrap}>
            <div className={s.filterGroup}>
              <label className={s.filterLabel} htmlFor="genres">
                Жанры:
              </label>
              <div className={s.filterSelectWrapper}>
                <select className={s.filterSelect} name="genres" id="genres">
                  {['Все категории', 'Экшены', 'Эдвенчуры'].map((i: string, id: number) => (
                    <option className={s.option} key={id} value={id}>
                      {i}
                    </option>
                  ))}
                </select>
              </div>
            </div>
            <div className={s.filterGroup}>
              <label className={s.filterLabel} htmlFor="sort">
                Сортировать по:
              </label>
              <div className={s.filterSelectWrapper}>
                <select className={s.filterSelect} name="sort" id="sort">
                  {['Актуальность', 'Новейшие', 'Старые'].map((i: string, id: number) => (
                    <option className={s.option} key={id} value={id}>
                      {i}
                    </option>
                  ))}
                </select>
              </div>
            </div>
          </div>
          <div className={s.sortResults}>Найдено 123 постов</div>
        </div>

        <div className={s.columns}>
          {[...new Array(11)].map((_, index) => (
            <div className="w-full" key={index}>
              <NewsItem
                title={'Главные 20 CS:GO игроков of 2023 согласно to Gspot.tv'}
                imageSrc={'https://loremflickr.com/640/400'}
                date={'2 часа назад'}
                category={'CS:GO'}
                size={'normal'}
                commentsCount={34}
                url={'#'}
              />
            </div>
          ))}
        </div>
      </section>
    </Section>
  )
}

export default NewsPage
