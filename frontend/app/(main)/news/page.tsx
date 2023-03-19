'use client'

import { Column80, Grid } from '@/components/Grid'
import React, { FC } from 'react'
import styled from 'styled-components'
import Post from './Post'

const Sort = styled.div`
    display: flex;
    margin-top: 200px;
    position: relative;
    padding: 20px;
    border-radius: 6px;
    border: 1px solid rgba(167, 130, 233, 0.06);
    margin-bottom: 10px;
`

const FilterGroup = styled.div`
    display: flex;
    gap: 20px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    width: 100%;
    margin-bottom: 30px;
    &:last-child {
        margin-bottom: 0;
    }
    width: auto;
    flex-direction: row;
    align-items: center;
    margin-bottom: 0;
    margin-right: 60px;
    &::last-child {
        margin-right: 0;
    }
`

const FilterLabel = styled.label`
    margin-top: 10px;
    font-size: 14px;
    line-height: 100%;
    letter-spacing: 0.4px;
    color: #dbdada;
    font-weight: normal;
    margin-bottom: 15px;
`

const FilterSelectWrap = styled.div`
    position: relative;
    width: 100%;
    width: 210px;
`

const FilterSelect = styled.select`
    width: 100%;
    height: 44px;
    border-radius: 6px;
    border: 1px solid rgba(167, 130, 233, 0.06);
    font-size: 14px;
    color: #fff;
    padding: 0 20px;
    cursor: pointer;
    background: url('../img/arrow2.svg') no-repeat center right 20px rgba(167, 130, 233, 0.03);
    background-size: 12px auto;
    letter-spacing: 0.4px;
`

const Option = styled.option`
    padding: 0;
    margin: 0;
    color: #000;
`

const SortResults = styled.div`
    margin-top: 10px;
    font-size: 14px;
    color: #dbdada;
    margin-left: auto;
`

const ColumnCards = styled.div`
    width: 100%;
    display: flex;
    flex-wrap: wrap;
`

const Page: FC<any> = ({}): JSX.Element => {
    return (
        <>
            <section className="section section--last section--catalog">
                <div className="container">
                    <Grid className="row">
                        <Column80 className="col-12">
                            <Sort>
                                <FilterGroup>
                                    <FilterLabel htmlFor="genres">Жанры:</FilterLabel>
                                    <FilterSelectWrap>
                                        <FilterSelect name="genres" id="genres">
                                            {['Все категории', 'Экшены', 'Эдвенчуры'].map((_: string, id: number) => (
                                                <Option key={id} value={id}>
                                                    {_}
                                                </Option>
                                            ))}
                                        </FilterSelect>
                                    </FilterSelectWrap>
                                </FilterGroup>
                                <FilterGroup>
                                    <FilterLabel htmlFor="sort">Сортировать по:</FilterLabel>
                                    <FilterSelectWrap>
                                        <FilterSelect name="sort" id="sort">
                                            {['Актуальность', 'Новейшие', 'Старые'].map((_: string, id: number) => (
                                                <Option key={id} value={id}>
                                                    {_}
                                                </Option>
                                            ))}
                                        </FilterSelect>
                                    </FilterSelectWrap>
                                </FilterGroup>
                                <SortResults>Найдено 123 постов</SortResults>
                            </Sort>
                        </Column80>
                    </Grid>
                    <ColumnCards>
                        {new Array(11).fill(0).map((_: number, id: number) => (
                            <Post key={id} />
                        ))}
                    </ColumnCards>
                </div>
            </section>
        </>
    )
}

export default Page
