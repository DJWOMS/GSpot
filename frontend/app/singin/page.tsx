'use client'

import React, { FC } from 'react'
import { Header, Grid, Column80 } from '@/components'
import styled from 'styled-components'

export const Sign__content = styled.div`
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 100%;
    min-height: 100vh;
    padding: 40px 0;
`

export const Sign__form = styled.form`
    background-color: #1b222e;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border: 1px solid rgba(167, 130, 233, 0.06);
    border-radius: 6px;
    padding: 40px 20px;
    position: relative;
    width: 100%;
    max-width: 400px;

    @media (min-width: 576px) {
        padding: 50px;
    }
`

const Sign__logo = styled.a`
    display: block;
    margin-bottom: 40px;
    transition: 0s;
`

const Sign__group = styled.div`
    position: relative;
    margin-bottom: 20px;
    width: 100%;
`

const Sign__btn = styled.button`
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 44px;
    border-radius: 6px;
    background-color: #29b474;
    color: #fff;
    font-weight: 600;
    font-size: 13px;
    letter-spacing: 0.6px;
    margin-top: 15px;
    margin-bottom: 15px;
    text-transform: uppercase;
    &:hover {
        background-color: #a782e9;
        color: #fff;
    }
`

const Sign__delimiter = styled.span`
    font-size: 13px;
    color: #dbdada;
    line-height: 100%;
`

const Sign__social = styled.div`
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    margin-bottom: 15px;
    margin-top: 15px;
`
const Sign__social_a = styled.a`
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    height: 44px;
    width: calc(33% - 10px);
    border-radius: 6px;
    color: #fff;
    background-color: #3b5999;
    &:hover {
        opacity: 0.7;
    }
`

const Sign__text = styled.span`
    margin-top: 15px;
    font-size: 14px;
    color: #dbdada;
    a {
        position: relative;
        color: #a782e9;
    }
    a:hover {
        color: #a782e9;
        text-decoration: underline;
    }
`

const Sign__input = styled.input`
    background-color: rgba(167, 130, 233, 0.03);
    border: 1px solid rgba(167, 130, 233, 0.06);
    border-radius: 6px;
    height: 44px;
    position: relative;
    color: #fff;
    font-size: 14px;
    width: 100%;
    padding: 0 20px;
    letter-spacing: 0.4px;
`

const Sign__group__checkbox = styled.div`
    position: relative;
    margin-bottom: 20px;
    width: 100%;
    width: 100%;
    text-align: left;
    color: #fff;
    input {
        font-size: 14px;
        color: #dbdada;
        font-weight: normal;
        position: relative;
        cursor: pointer;
        padding-left: 35px;
        line-height: 20px;
        margin: 0;
        position: absolute;
        left: -9999px;
        color: #a782e9;
    }
`

const SignIn: FC<any> = ({}): JSX.Element => {
    return (
        <>
            <Header />
            <section className="section section--last section--catalog">
                <div className="container">
                    <Grid className="row">
                        <Column80 className="col-12">
                            <Sign__content>
                                <Sign__form>
                                    <Sign__logo>
                                        <img src="img/logo.svg" alt="" />
                                    </Sign__logo>
                                    <Sign__group>
                                        <Sign__input type="text" placeholder="Email" />
                                    </Sign__group>
                                    <Sign__group>
                                        <Sign__input type="password" placeholder="Password" />
                                    </Sign__group>
                                    <Sign__group__checkbox>
                                        <input id="remember" name="remember" type="checkbox" />
                                        <label>Запомнить меня</label>
                                    </Sign__group__checkbox>
                                    <Sign__btn>Sign in</Sign__btn>
                                    <Sign__delimiter>or</Sign__delimiter>
                                    <Sign__social>
                                        <Sign__social_a href="#">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="512" viewBox="0 0 512 512">
                                                <path d="M455.27,32H56.73A24.74,24.74,0,0,0,32,56.73V455.27A24.74,24.74,0,0,0,56.73,480H256V304H202.45V240H256V189c0-57.86,40.13-89.36,91.82-89.36,24.73,0,51.33,1.86,57.51,2.68v60.43H364.15c-28.12,0-33.48,13.3-33.48,32.9V240h67l-8.75,64H330.67V480h124.6A24.74,24.74,0,0,0,480,455.27V56.73A24.74,24.74,0,0,0,455.27,32Z" />
                                            </svg>
                                        </Sign__social_a>
                                        <Sign__social_a href="#">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="512" viewBox="0 0 512 512">
                                                <path d="M496,109.5a201.8,201.8,0,0,1-56.55,15.3,97.51,97.51,0,0,0,43.33-53.6,197.74,197.74,0,0,1-62.56,23.5A99.14,99.14,0,0,0,348.31,64c-54.42,0-98.46,43.4-98.46,96.9a93.21,93.21,0,0,0,2.54,22.1,280.7,280.7,0,0,1-203-101.3A95.69,95.69,0,0,0,36,130.4C36,164,53.53,193.7,80,211.1A97.5,97.5,0,0,1,35.22,199v1.2c0,47,34,86.1,79,95a100.76,100.76,0,0,1-25.94,3.4,94.38,94.38,0,0,1-18.51-1.8c12.51,38.5,48.92,66.5,92.05,67.3A199.59,199.59,0,0,1,39.5,405.6,203,203,0,0,1,16,404.2,278.68,278.68,0,0,0,166.74,448c181.36,0,280.44-147.7,280.44-275.8,0-4.2-.11-8.4-.31-12.5A198.48,198.48,0,0,0,496,109.5Z" />
                                            </svg>
                                        </Sign__social_a>
                                        <Sign__social_a href="#">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="512" viewBox="0 0 512 512">
                                                <path d="M473.16 221.48l-2.26-9.59H262.46v88.22H387c-12.93 61.4-72.93 93.72-121.94 93.72-35.66 0-73.25-15-98.13-39.11a140.08 140.08 0 01-41.8-98.88c0-37.16 16.7-74.33 41-98.78s61-38.13 97.49-38.13c41.79 0 71.74 22.19 82.94 32.31l62.69-62.36C390.86 72.72 340.34 32 261.6 32c-60.75 0-119 23.27-161.58 65.71C58 139.5 36.25 199.93 36.25 256s20.58 113.48 61.3 155.6c43.51 44.92 105.13 68.4 168.58 68.4 57.73 0 112.45-22.62 151.45-63.66 38.34-40.4 58.17-96.3 58.17-154.9 0-24.67-2.48-39.32-2.59-39.96z" />
                                            </svg>
                                        </Sign__social_a>
                                    </Sign__social>
                                    <Sign__text>
                                        У вас нет аккаунта? <a href="signup.html">Зарегистрироваться!</a>
                                    </Sign__text>
                                    <Sign__text>
                                        <a href="forgot.html">Забыли пароль?</a>
                                    </Sign__text>
                                </Sign__form>
                            </Sign__content>
                        </Column80>
                    </Grid>
                </div>
            </section>
        </>
    )
}

export default SignIn
