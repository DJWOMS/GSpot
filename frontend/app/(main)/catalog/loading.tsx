import React, { FC } from 'react'
import { Group, Label, Select } from 'components/Form'
import Pagination from 'components/Pagination'
import Section from 'components/Section'
import { SkeletonCheckBox, SkeletonInput, SkeletonListCheckBoxes, SkeletonSelect } from 'components/Skeleton'
import { SkeletonGameCard } from 'components/Skeleton/SkeletonGameCard'
import { FilterGames, GameCard, GameCardInterface, GameListInterface, generateMockGameList } from 'features/games'
import s from './/page.module.scss'

export default function Loading() {
  const items = new Array(8).fill('', 0)
  const filters = new Array(17).fill('', 0)
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
            {filters.map((index, id) => (
              <SkeletonInput size={'44'} key={index} />
            ))}
          </div>
          <div className={s.columns10}>
            <div className={s.list}>
              {items.map((index, id) => (
                <SkeletonGameCard key={index} />
              ))}
            </div>
            <Pagination />
          </div>
        </div>
      </Section>
    </>
  )
}
{
  /*
(
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
            <Section last>
              <div className={s.row}>
                <div className={s.columns2}>
                  <>
                    <button className={s.openFilter}></button>
                    <div>
                      <form className={s.components}>
                        <h4 className={s.title}>
                          Фильтры
                          <button className={s.clearFilters}>Сбросить</button>
                        </h4>
                        <Group>
                          <Label>Сортировать: </Label>
                          <SkeletonSelect />
                        </Group>

                        <Group>
                          <Label>Цена: </Label>
                          <>
                            <SkeletonInput size="28" />
                            <SkeletonInput />
                          </>
                        </Group>

                        <Group>
                          <Label>Платформа: </Label>
                          <SkeletonListCheckBoxes count={4} />
                        </Group>
                        <Group>
                          <Label>Жанры:</Label>

                          <SkeletonListCheckBoxes count={7} />
                          <>
                            <div className="mb-5 ml-5"></div>
                          </>
                        </Group>

                        <Group>
                          <button className={s.applyFilter} type="submit">
                            Применить фильтр
                          </button>
                        </Group>
                      </form>
                    </div>
                  </>
                </div>
              </div>
            </Section>
          </div>
          <div className={s.columns10}>
            <div className={s.list}>
              <SkeletonGameCard />
              <SkeletonGameCard />
              <SkeletonGameCard />
              <SkeletonGameCard />
              <SkeletonGameCard />
            </div>
          </div>
        </div>
      </Section>
    </>
  )


*/
}
