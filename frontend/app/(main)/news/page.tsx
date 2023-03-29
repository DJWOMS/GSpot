import { FC } from 'react'
import Breadcrumbs from 'components/Breadcrumbs'
import Section from 'components/Section'
import { NewsItem } from 'features/news'
import s from './page.module.scss'

const NewsPage: FC = () => {
  return (
    <Section
      items={[
        {
          title: 'Новости',
          navigation: [
            {
              children: <Breadcrumbs items={[{ name: 'Новости' }]} />,
            },
          ],
          children: (
            <section className="section section--last section--catalog">
              <div className={s.sort}>
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
                <div className={s.sortResults}>Найдено 123 постов</div>
              </div>

              <div className={s.columns}>
                {new Array(11).fill(0).map((_: number, id: number) => (
                  <div className="w-full" key={id}>
                    <NewsItem
                      title={'Главные 20 CS:GO игроков of 2023 согласно to Gspot.tv'}
                      imageSrc={'https://loremflickr.com/240/320'}
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
          ),
        },
      ]}
    />
  )
}

export default NewsPage
