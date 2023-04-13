import s from 'app/(main)/catalog/page.module.scss'
import Pagination from 'components/Pagination'
import Section from 'components/Section'
import { FilterGames, GameCard, GameCardInterface } from 'features/games'
import { fetchServerSide } from 'lib/fetchServerSide'

const FavoritesPage = async () => {
  const favorites = await fetchServerSide<GameCardInterface[]>({
    path: '/profile/favorites',
  })
  return (
    <>
      <Section title={'Favorites'}>
        <Section last>
          <div className={s.row}>
            <div className={s.columns2}>
              <FilterGames />
            </div>

            <div className={s.columns10}>
              <div className={s.list}>
                {favorites?.map((game, id) => (
                  <GameCard actionType={'delete'} {...game} key={id} />
                ))}
              </div>

              <Pagination />
            </div>
          </div>
        </Section>
      </Section>
    </>
  )
}
export default FavoritesPage
