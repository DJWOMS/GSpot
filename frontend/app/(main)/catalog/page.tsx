import Pagination from 'components/Pagination'
import Section from 'components/Section'
import { GameCard, FilterGames, GameCardInterface } from 'features/games'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from './page.module.scss'

// revalidate data every 60sec
export const revalidate = 60

const CatalogPage = async ({ searchParams }: { searchParams: URLSearchParams }) => {
  const data = await fetchServerSide<GameCardInterface[]>({
    path: `/games/list?${new URLSearchParams(searchParams)}`,
    cache: 'no-cache',
  })

  return (
    <>
      <Section
        title={
          <>
            Каталог <span>(35430 игр)</span>
          </>
        }
      />

      <Section last>
        <div className={s.row}>
          <div className={s.columns2}>
            <FilterGames />
          </div>

          <div className={s.columns10}>
            <div className={s.list}>
              {data?.map(({ title, coverImg, price, link }, id) => (
                <GameCard title={title} coverImg={coverImg} link={link} badge="New" price={price} sale={15} key={id} />
              ))}
            </div>

            <Pagination />
          </div>
        </div>
      </Section>
    </>
  )
}

export default CatalogPage
