import React from 'react'
import { Group, Label } from 'components/Form'
import Section from 'components/Section'
import { SkeletonInput, SkeletonListCheckBoxes, SkeletonSelect } from 'components/Skeleton'
import { SkeletonCard } from 'components/Skeleton'
import s from './page.module.css'

export default function Loading() {
  return (
    <>
      <Section title={<>Каталог</>} />
      <Section last>
        <div className={s.row}>
          <div className={s.columns2}>
            <div className="hidden lg:block">
              <div className="mb-[10px] flex flex-col items-start justify-start">
                <h4
                  className="mb-[25px] flex h-auto w-full flex-row items-center justify-between text-base font-semibold
    tracking-default text-white"
                >
                  Фильтры
                  <button className="text-[12px] font-normal tracking-[0px] text-primary" type="button">
                    Сбросить
                  </button>
                </h4>

                <Group>
                  <Label>Сортировать: </Label>
                  <SkeletonSelect />
                </Group>

                <Group>
                  <Label>Цена: </Label>
                  <SkeletonInput size="28" />
                  <SkeletonInput />
                </Group>

                <Group>
                  <Label>Платформа: </Label>
                  <SkeletonListCheckBoxes count={4} />
                </Group>

                <Group>
                  <Label>Жанры:</Label>
                  <SkeletonListCheckBoxes count={7} />
                </Group>

                <Group>
                  <button
                    className="flex h-[44px] w-full flex-row items-center justify-center rounded-default border
    border-solid border-main-400 bg-main-30 tracking-[.4px] text-white"
                    type="submit"
                  >
                    Применить фильтр
                  </button>
                </Group>
              </div>
            </div>
          </div>
          <div className={s.columns10}>
            <div className={s.list}>
              {[...new Array(11)].map((_, index) => (
                <SkeletonCard key={index} />
              ))}
            </div>
          </div>
        </div>
      </Section>
    </>
  )
}
