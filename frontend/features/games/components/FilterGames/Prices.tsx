import { useEffect, useState } from 'react'
import { Group, Label } from 'components/Form'
import { SkeletonInput } from 'components/Skeleton'
import { Range } from 'components/Slider'
import { FormPriceType } from 'features/games'
import { useFilter } from 'features/games/store'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from './Prices.module.scss'

const Prices = () => {
  const [defaultPrices, setDefaultPrices] = useState<FormPriceType[] | null>(null)
  const [prices, setPrices] = useState<FormPriceType[]>([])

  const { getFilter, setFilter } = useFilter((state) => ({ getFilter: state.getFilter, setFilter: state.setFilter }))

  useEffect(() => {
    const loadData = async () => {
      const response = await fetchServerSide<FormPriceType[]>({
        path: '/games/filters/prices',
      })

      if (response) {
        const selectedPrices = getFilter('prices')

        setPrices(selectedPrices.length > 0 ? selectedPrices : response)
        setDefaultPrices(response)
      }
    }

    loadData()
  }, [getFilter])

  const handlePriceChange = (_value: number | FormPriceType[]) => {
    const value = _value as FormPriceType[]

    setPrices(value)
    setFilter('prices', value)
  }

  return (
    <Group>
      <Label>Цена: </Label>

      {defaultPrices === null ? (
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

          <Range min={0} max={1000} defaultValue={[100, 500]} value={prices} onChange={handlePriceChange} />
        </>
      )}
    </Group>
  )
}

export { Prices }
