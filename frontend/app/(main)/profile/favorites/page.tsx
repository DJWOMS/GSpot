'use client'

import { useEffect, useState } from 'react'
import Pagination from 'components/Pagination'
import Section from 'components/Section'
import { GameCard } from 'features/games/components'
import type { GameCardInterface } from 'features/games/types'
import { fetchServerSide } from 'lib/fetchServerSide'
import { useRouter, useSearchParams } from 'next/navigation'
import s from './page.module.css'

const FavoritesPage = () => {
  const [favorites, setFavorites] = useState<GameCardInterface[]>([])
  const router = useRouter()
  const searchParams = useSearchParams()
  const currentPage = searchParams.get('page') ? Number(searchParams.get('page')) : 1
  const fetchData = async () => {
    const data = await fetchServerSide<GameCardInterface[]>({
      path: '/profile/favorites',
    })
    setFavorites(data as GameCardInterface[])
  }
  const onDelete = async () => {
    await fetchServerSide({
      method: 'DELETE',
      path: '/profile/favorites',
    })
    fetchData()
    router.refresh()
  }
  useEffect(() => {
    fetchData()
  }, [])
  return (
    <Section title={'Favorites'}>
      <div className={s.columns10}>
        <div className={s.list}>
          {favorites.map((game, index) => (
            <GameCard onDelete={onDelete} {...game} key={index} />
          ))}
        </div>
        <Pagination
          path={'/profile/favorites'}
          currentPage={currentPage}
          visiblePageButtonsCount={5}
          pageCount={5}
        />
      </div>
    </Section>
  )
}
export default FavoritesPage
