'use client'

import { useEffect, useState } from 'react'
import cn from 'classnames'
import { Group } from 'components/Form'
import { useFilter } from 'features/games/store'
import { useRouter, useSearchParams } from 'next/navigation'
import queryString from 'query-string'
import s from './FilterGames.module.scss'
import { Genres } from './Genres'
import { Keywords } from './Keywords'
import { Platforms } from './Platforms'
import { Prices } from './Prices'
import { SortBy } from './SortBy'

const FilterGames = () => {
  const queryParams = useSearchParams()

  // set filter values
  const getFilters = useFilter((state) => state.getFilters)
  const setFilters = useFilter((state) => state.setFilters)

  useEffect(() => {
    setFilters(queryParams)
  }, [queryParams, setFilters])

  // update router if needed
  const router = useRouter()

  const onSubmitForm = () => router.push(`/catalog?${queryString.stringify(getFilters(), { skipNull: true })}`)

  const [openMobileFilter, setOpenMobileFilter] = useState(false)
  const toggleMobileFilter = () => setOpenMobileFilter((state) => !state)

  return (
    <>
      <button className={s.openFilter} onClick={toggleMobileFilter}>
        {!openMobileFilter ? 'Открыть фильтр' : 'Скрыть фильтр'}
      </button>

      <div className={cn(s.wrapper, { [s.open]: openMobileFilter })}>
        <div onSubmit={onSubmitForm} className={s.components}>
          <h4 className={s.title}>Фильтры</h4>

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
