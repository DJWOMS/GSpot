'use client'

import Link from 'next/link'

import { IconBrandFacebook, IconBrandGoogle, IconBrandTwitter } from '@tabler/icons-react'
import { Form, SignCheckbox, SignGroup, SignInput, SignBtn, SignDelimiter, SignSocial, SignSocials, SignText } from '../Form'

export default function Signin() {
    return (
        <Form onSubmit={() => console.log('hello')}>
            <SignGroup>
                <SignInput type="text" placeholder="Введите username" />
            </SignGroup>

            <SignGroup>
                <SignInput type="email" placeholder="Введите email" />
            </SignGroup>

            <SignGroup>
                <SignInput type="password" placeholder="Введите пароль" />
            </SignGroup>

            <SignCheckbox>
                <input id="remember" />
                <label htmlFor="remember">Запомнить меня</label>
            </SignCheckbox>

            <SignBtn>Авторизация</SignBtn>
            <SignDelimiter>или</SignDelimiter>

            <SignSocials>
                <SignSocial color="fb">
                    <IconBrandFacebook />
                </SignSocial>

                <SignSocial color="gl">
                    <IconBrandGoogle />
                </SignSocial>

                <SignSocial color="tw">
                    <IconBrandTwitter />
                </SignSocial>
            </SignSocials>

            <SignText>
                Еще нет аккаунта? <Link href="/signup">Регистрация</Link>
            </SignText>

            <SignText>
                <Link href="/forgot">Забыли пароль?</Link>
            </SignText>
        </Form>
    )
}
