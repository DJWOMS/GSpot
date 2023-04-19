import Pagination from 'components/Pagination'
import Section from 'components/Section'
import { GameCard, GameCardInterface } from 'features/games'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from './page.module.scss'

const FavoritesPage = async () => {
  const favorites = await fetchServerSide<GameCardInterface[]>({
    path: '/profile/favorites',
  })
  return (
    <>
      <Section title={'Favorites'}>
        <Section last>
          <div className={s.columns10}>
            <div className={s.list}>
              {favorites?.map((game, index) => (
                <GameCard favorite {...game} key={index} />
              ))}
            </div>

            <Pagination />
          </div>
        </Section>
      </Section>
    </>
  )
}
export default FavoritesPage
