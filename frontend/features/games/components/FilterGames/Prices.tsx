import { useEffect, useState } from 'react'
import { Group, Label } from 'components/Form'
import { SkeletonInput } from 'components/Skeleton'
import { FormPriceType } from 'features/games'
import { useFilter } from 'features/games/store'
import { fetchServerSide } from 'lib/fetchServerSide'
import Slider from 'rc-slider'
import 'rc-slider/assets/index.css'
import s from './FilterGames.module.scss'

const Prices = () => {
  const [prices, setPrices] = useState<FormPriceType[] | null>(null)

  useEffect(() => {
    const loadData = async () => {
      const response = await fetchServerSide<FormPriceType[]>({
        path: '/games/filters/prices',
      })

      if (response) {
        setPrices(response)
      }
    }

    loadData()
  }, [])

  const setFilter = useFilter((state) => state.setFilter)

  const handlePriceChange = (_value: number | FormPriceType[]) => {
    const value = _value as FormPriceType[]

    setPrices(value)
    setFilter('prices', value)
  }

  return (
    <Group>
      <Label>Цена: </Label>

      {prices === null ? (
        <>
          <SkeletonInput size="28" />
          <SkeletonInput />
        </>
      ) : (
        <>
          <div className={s.range}>
            <div id="filter__range-start">{prices[0]}</div>
            <div id="filter__range-end">{prices[1]}</div>
          </div>

          <Slider range min={0} max={1000} defaultValue={[100, 500]} value={prices} onChange={handlePriceChange} />
        </>
      )}
    </Group>
  )
}

export { Prices }
