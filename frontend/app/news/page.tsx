'use client'

import { Column80, Grid, Header } from '@/components'
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

const Filter__group = styled.div`
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

const Filter__label = styled.label`
    margin-top: 10px;
    font-size: 14px;
    line-height: 100%;
    letter-spacing: 0.4px;
    color: #dbdada;
    font-weight: normal;
    margin-bottom: 15px;
`

const Filter__select_wrap = styled.div`
    position: relative;
    width: 100%;
    width: 210px;
`

const Filter__select = styled.select`
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
    option {
        padding: 0;
        margin: 0;
        color: #000;
    }
`

const Sort__results = styled.div`
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
            <Header />
            <section className="section section--last section--catalog">
                <div className="container">
                    <Grid className="row">
                        <Column80 className="col-12">
                            <Sort>
                                <Filter__group>
                                    <Filter__label htmlFor="genres">Genres:</Filter__label>
                                    <Filter__select_wrap>
                                        <Filter__select name="genres" id="genres">
                                            <option value="0">Все категории</option>
                                            <option value="1">Экшены</option>
                                            <option value="3">Эдвенчуры</option>
                                        </Filter__select>
                                    </Filter__select_wrap>
                                </Filter__group>
                                <Filter__group>
                                    <Filter__label htmlFor="sort">Сортировать по:</Filter__label>
                                    <Filter__select_wrap>
                                        <Filter__select name="sort" id="sort">
                                            <option value="0">Relevance</option>
                                            <option value="1">Newest</option>
                                            <option value="2">Oldest</option>
                                        </Filter__select>
                                    </Filter__select_wrap>
                                </Filter__group>
                                <Sort__results>Найдено 123 постов</Sort__results>
                            </Sort>
                        </Column80>
                    </Grid>
                    <ColumnCards>
                        <Post />
                        <Post />
                        <Post />
                        <Post />
                        <Post />
                        <Post />
                        <Post />
                    </ColumnCards>
                </div>
            </section>
        </>
    )
}

export default Page
