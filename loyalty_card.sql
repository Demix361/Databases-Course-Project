PGDMP     #                    x            shop_v3    12.4    12.4     R           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            S           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            T           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            U           1262    16653    shop_v3    DATABASE     �   CREATE DATABASE shop_v3 WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Russian_Russia.1251' LC_CTYPE = 'Russian_Russia.1251';
    DROP DATABASE shop_v3;
                postgres    false            �            1259    16728    users_loyaltycard    TABLE     �   CREATE TABLE public.users_loyaltycard (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    discount double precision NOT NULL
);
 %   DROP TABLE public.users_loyaltycard;
       public         heap    postgres    false            �            1259    16731    users_loyaltycard_id_seq    SEQUENCE     �   CREATE SEQUENCE public.users_loyaltycard_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.users_loyaltycard_id_seq;
       public          postgres    false    225            V           0    0    users_loyaltycard_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.users_loyaltycard_id_seq OWNED BY public.users_loyaltycard.id;
          public          postgres    false    226            �
           2604    16754    users_loyaltycard id    DEFAULT     |   ALTER TABLE ONLY public.users_loyaltycard ALTER COLUMN id SET DEFAULT nextval('public.users_loyaltycard_id_seq'::regclass);
 C   ALTER TABLE public.users_loyaltycard ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    226    225            N          0    16728    users_loyaltycard 
   TABLE DATA           ?   COPY public.users_loyaltycard (id, name, discount) FROM stdin;
    public          postgres    false    225   \       W           0    0    users_loyaltycard_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.users_loyaltycard_id_seq', 6, true);
          public          postgres    false    226            �
           2606    16790 (   users_loyaltycard users_loyaltycard_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.users_loyaltycard
    ADD CONSTRAINT users_loyaltycard_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.users_loyaltycard DROP CONSTRAINT users_loyaltycard_pkey;
       public            postgres    false    225            N   |   x�5�A�@�ӏ!���kx.G�ɛ��	Q����فx�I�:5�x��g��/?q�Te$㓃���?s^Q��x�r��Ew��7^�|�ɲS@6>�v�}���c��x��Go�,"���+ ?�yT�     