'use client'

import { useEffect } from 'react'
import { Group } from 'components/Form'
import { useFilter } from 'features/games/store'
import { useRouter, useSearchParams } from 'next/navigation'
import qs from 'qs'
import s from './FilterGames.module.scss'
import { Genres } from './Genres'
import { Keywords } from './Keywords'
import { Platforms } from './Platforms'
import { Prices } from './Prices'
import { SortBy } from './SortBy'

const FilterGames = () => {
  const queryParams = useSearchParams()

  // set filter values
  const { getFilters, setFilters } = useFilter((state) => ({ getFilters: state.getFilters, setFilters: state.setFilters }))
  useEffect(() => {
    setFilters(queryParams)
  }, [queryParams, setFilters])

  // update router if needed
  const router = useRouter()
  const onSubmitForm = () => {
    router.push(`/catalog?${qs.stringify(getFilters(), { skipNulls: true })}`)
  }

  return (
    <>
      <button className={s.openFilter}>Открыть фильтр</button>

      <div className={s.wrapper}>
        <div onSubmit={onSubmitForm} className={s.components}>
          <h4 className={s.title}>
            Фильтры <button className={s.clearFilters}>Очистить</button>
          </h4>

          <Keywords />
          <SortBy />
          <Prices />
          <Platforms />
          <Genres />

          <Group>
            <button className={s.applyFilter} onClick={onSubmitForm}>
              Применить фильтр
            </button>
          </Group>
        </div>
      </div>
    </>
  )
}

export { FilterGames }
