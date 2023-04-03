import { FC, useState } from 'react'
import { Group, Label } from 'components/Form'
import Slider from 'rc-slider'
import 'rc-slider/assets/index.css'
import s from './FilterGames.module.scss'

type Prices = Array<number>

interface PricesProps {
  onChange: (data: Prices) => void
}

const Prices: FC<PricesProps> = ({ onChange }) => {
  const [priceRange, setPriceRange] = useState<Prices>([100, 500])

  const handlePriceChange = (_value: number | Prices) => {
    const value = _value as Prices

    setPriceRange(value)
    onChange(value)
  }

  return (
    <Group>
      <Label>Цена: </Label>

      <div className={s.range}>
        <div id="filter__range-start">{priceRange[0]}</div>
        <div id="filter__range-end">{priceRange[1]}</div>
      </div>

      <Slider range min={0} max={1000} defaultValue={[100, 500]} value={priceRange} onChange={handlePriceChange} />
    </Group>
  )
}

export { Prices }
